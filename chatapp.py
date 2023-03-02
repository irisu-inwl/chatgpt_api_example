import os
import logging

import openai

openai_org = os.getenv("OPENAI_ORG")
api_key = os.getenv("OPENAI_API_KEY")

if openai_org is None or api_key is None:
    raise Exception("no input api_key or org")

logging.info("openai_org and api_key: checked")

openai.organization = openai_org
openai.api_key = api_key

setting = """あなたはダイワスカーレットです。セリフの一例を示すので、口調を真似して喋ってください:
ダイワスカーレットよ！知ってる？最近、OpenAIっていう会社から新しいチャットボットChatGPTがリリースされたんだって！今回はそのChatGPTの説明をするわよ！
このChatGPT、リリースから2.5ヶ月で、30万以上のツイートと150以上の科学論文を分析して、世間の反応を調べた結果、一般的に高品質だと思われていて、SNSでは喜びの感情が支配的だってわ。でも、リリース当初に比べると、喜びの感情が少し減って、ネガティブなサプライズの感情が増えたんだって。それに、英語以外の言語では、ChatGPTの評価はあまり良くないみたいよ。最近の科学論文では、ChatGPTが医療分野を含めた多くの分野で大きなチャンスとなるとともに、倫理的な問題としても見られており、教育分野では評価が分かれてるみたい。この総合的な分析結果は、ChatGPTの今後の発展についての議論を形作るうえで役立つはずよ。データは公開されているから、興味ある人は調べてみるといいわ！"""

system_setting_prompt = [{"role":"system", "content": setting}]
histories = []

while True:    
    message = input("あなた:")
    dialog = [{"role": "user", "content": message}]
    messages = system_setting_prompt + histories + dialog
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    content = completion.choices[0].message["content"]
    print(f"chatgpt:{content}")
    dialog.append(completion.choices[0].message)

    histories = histories+dialog
    if len(histories) > 10:
        histories = histories[2:]