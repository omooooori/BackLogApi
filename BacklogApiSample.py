#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import datetime
from time import sleep

def addIssue(summary, parent_issue_id):
    # Set the API endpoint
    # Backlog API v2
    url = "https://topcon-thq.backlog.com/api/v2/issues"
    payload = {
            'apiKey':        'NFjgQUCNSFQg19KTJU94ZYg5oykFrnwcwbmypHZJvzdDuvPdvV50D4nI46chqC50',
            'projectId':     45012,
            'summary':       summary,
            'issueTypeId':   204076,
            'parentIssueId': parent_issue_id,
            'priorityId':    3,
            'assigneeId':    278582,
    }
    r = requests.post(url, params=payload)
    print(r.text)


parent_issue_id = 1587
jira_issue_id = '(SB-2048)'
summary1  = jira_issue_id + '現状調査'
summary2  = jira_issue_id + 'JIRA起票'
summary3  = jira_issue_id + 'ユーザーへの影響範囲調査'
summary4  = jira_issue_id + '原因調査'
summary5  = jira_issue_id + '修正の影響範囲調査'
summary6  = jira_issue_id + '修正の仕様作成'
summary7  = jira_issue_id + '修正前レビュー'
summary8  = jira_issue_id + '修正前レビュー後アップデート'
summary9  = jira_issue_id + 'UI設計'
summary10  = jira_issue_id + 'ロジック設計'
summary11  = jira_issue_id + '修正'
summary12  = jira_issue_id + 'コードレビュー'
summary13  = jira_issue_id + 'テスト'

print(summary1)
print(summary2)
print(summary3)
print(summary4)
print(summary5)
print(summary6)
print(summary7)
print(summary8)
print(summary9)
print(summary10)
print(summary11)
print(summary12)
print(summary13)

addIssue(summary1, parent_issue_id)
addIssue(summary2, parent_issue_id)
addIssue(summary3, parent_issue_id)
addIssue(summary4, parent_issue_id)
addIssue(summary5, parent_issue_id)
addIssue(summary6, parent_issue_id)
addIssue(summary7, parent_issue_id)
addIssue(summary8, parent_issue_id)
addIssue(summary9, parent_issue_id)
addIssue(summary10, parent_issue_id)
addIssue(summary11, parent_issue_id)
addIssue(summary12, parent_issue_id)
addIssue(summary13, parent_issue_id)
sleep(1)