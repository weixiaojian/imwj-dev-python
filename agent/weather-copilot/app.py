import os
import json
from datetime import datetime, timedelta
from openai import OpenAI
from pathlib import Path
from dotenv import load_dotenv

# 加载配置
load_dotenv(Path(__file__).with_name(".env"))
# 初始化client
client = OpenAI()

# 查询天气方法
def get_weather(city: str, date: str = "today") -> dict:
    """
    查询指定城市的天气
    Args：
        city: 城市名称
        date: 日期，“today”、“tomorrw”、“YYYY-MM-DD”
    Return：
        包含天气信息的回复
    """

    # 模拟天气数据
    weather_data = {
        "北京": {"today": ("晴", 25), "tomorrow": ("多云", 23)},
        "上海": {"today": ("小雨", 28), "tomorrow": ("阴", 27)},
        "广州": {"today": ("雷阵雨", 31), "tomorrow": ("晴", 33)},
        "深圳": {"today": ("台风", 31), "tomorrow": ("晴", 33)},
    }

    # 处理日期
    if date == "today":
        date_key = "today"
    elif date == "tomorrow":
        date_key = "tomorrow"
    else:
        # 如果是具体日期，简化为 today
        date_key = "today"

    # 处理城市不在范围内
    if city not in weather_data:
        return {"error": f"暂不支持查询{city}的天气！"}

    # 获取天气数据
    weather, temp = weather_data[city][date_key]

    return {
        "city": city,
        "date": date,
        "weather": weather,
        "temperature": f"{temp}°C",
    }

# 工具情况定义
tools_schema = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "查询指定城市指定日期的天气信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "城市名称，如 北京、上海、广州"
                    },
                    "date": {
                        "type": "string",
                        "description": "日期，可以是 today、tomorrow 或 YYYY-MM-DD 格式",
                        "default": "today"
                    }
                },
                "required": ["city"]
            }
        }
    }
]

def run_agent(user_msg: str) -> str:
    """运行 Agent：感知 -> 决策 -> 行动 -> 观察"""
    messages = [
        {"role": "system", "content": "你是一个天气助手，帮用户查询天气，用自然语气回答"},
        {"role": "user", "content": user_msg},
    ]

    # === Agent循环 ===
    while True:
        # 1.感知 + 决策：
        response = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL"),
            messages=messages,
            tools=tools_schema,
        )

        msg = response.choices[0].message

        # 2.判断：AI是否调用工具
        if not msg.tool_calls:
            return msg.content

        # 3.行动：AI要调用工具 -> 执行工具
        messages.append(msg) # 先吧AI的消息加入历史

        for tool_call in msg.tool_calls:
            # 解析工具名和参数名
            func_name = tool_call.function.name
            func_args = json.loads(tool_call.function.arguments)

            print(f"🔧 调用工具: {func_name}({func_args})")

            # 执行工具
            if func_name == "get_weather":
                result = get_weather(**func_args)
            else:
                result = {"error": f"未知工具: {func_name}"}

            # 4.观察：把工具结果返回给AI
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result, ensure_ascii=False),
            })

        # 循环回去 -> AI看到工具结果，决定下一步

# === 测试 ===
print(run_agent("深圳"))
