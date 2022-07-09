# import schedule
# import time
# from datetime import datetime
# from slack_sdk import WebClient
# import datetime as dt
#
# class SlackAPI:
#     """
#     슬랙 API 핸들러
#     """
#
#     def __init__(self, token):
#         # 슬랙 클라이언트 인스턴스 생성
#         self.client = WebClient(token)
#
#     def get_channel_id(self, channel_name):
#         """
#         슬랙 채널ID 조회
#         """
#         # conversations_list() 메서드 호출
#         result = self.client.conversations_list()
#         # 채널 정보 딕셔너리 리스트
#         channels = result.data['channels']
#         # 채널 명이 'test'인 채널 딕셔너리 쿼리
#         channel = list(filter(lambda c: c["name"] == channel_name, channels))[0]
#         # 채널ID 파싱
#         channel_id = channel["id"]
#         return channel_id
#
#     def get_message_ts(self, channel_id, query):
#         """
#         슬랙 채널 내 메세지 조회
#         """
#         # conversations_history() 메서드 호출
#         result = self.client.conversations_history(channel=channel_id)
#         # 채널 내 메세지 정보 딕셔너리 리스트
#         messages = result.data['messages']
#         # 채널 내 메세지가 query와 일치하는 메세지 딕셔너리 쿼리
#         message = list(filter(lambda m: m["text"] == query, messages))[0]
#         # 해당 메세지ts 파싱
#         message_ts = message["ts"]
#         return message_ts
#
#     def post_thread_message(self, channel_id, message_ts, text):
#         """
#         슬랙 채널 내 메세지의 Thread에 댓글 달기
#         """
#         # chat_postMessage() 메서드 호출
#         result = self.client.chat_postMessage(
#             channel=channel_id,
#             text=text,
#             thread_ts=message_ts
#         )
#         return result
#
#     def post_message(self, channel_id, text):
#         result = self.client.chat_postMessage(
#             channel=channel_id,
#             text=text
#         )
#         return result
#
#
# def job():
#     channel_name = "출퇴근"
#     message = datetime.today().strftime("%Y년 %m월 %d일 출퇴근 스레드")
#     slack.post_message(channel_name, message)
#
#
# if __name__ == '__main__':
#     slack = SlackAPI(token)
#     slack.post_message("출퇴근", "slack bot 자동화 시작")
#     t = "08:00"
#     schedule.every().monday.at(t).do(job)
#     schedule.every().tuesday.at(t).do(job)
#     schedule.every().wednesday.at(t).do(job)
#     schedule.every().thursday.at(t).do(job)
#     schedule.every().friday.at(t).do(job)
#     while True:
#         schedule.run_pending()
#         time.sleep(1)
#
#
#
