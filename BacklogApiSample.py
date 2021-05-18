#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from time import sleep

def addIssueImpl(summary, parent_issue_id, issue_type_id):
    url = "https://topcon-thq.backlog.com/api/v2/issues"
    payload = {
            'apiKey':        'NFjgQUCNSFQg19KTJU94ZYg5oykFrnwcwbmypHZJvzdDuvPdvV50D4nI46chqC50',
            'projectId':     45012,
            'summary':       summary,
            'issueTypeId':   issue_type_id,
            'parentIssueId': parent_issue_id,
            'priorityId':    3,
            'assigneeId':    278582,
    }
    r = requests.post(url, params=payload)
    print(r.text)


def addDefectIssue():
    parent_issue_id = 12449537
    jira_issue_id = '(SB-2044)'
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

    issue_type_id = 204076

    addIssueImpl(summary1, parent_issue_id, issue_type_id)
    sleep(1)
    addIssueImpl(summary2, parent_issue_id, issue_type_id)
    sleep(1)
    addIssueImpl(summary3, parent_issue_id, issue_type_id)
    sleep(1)
    addIssueImpl(summary4, parent_issue_id, issue_type_id)
    sleep(1)
    addIssueImpl(summary5, parent_issue_id, issue_type_id)
    sleep(1)
    addIssueImpl(summary6, parent_issue_id, issue_type_id)
    sleep(1)
    addIssueImpl(summary7, parent_issue_id, issue_type_id)
    sleep(1)
    addIssueImpl(summary8, parent_issue_id, issue_type_id)
    sleep(1)
    addIssueImpl(summary9, parent_issue_id, issue_type_id)
    sleep(1)
    addIssueImpl(summary10, parent_issue_id, issue_type_id)
    sleep(1)
    addIssueImpl(summary11, parent_issue_id, issue_type_id)
    sleep(1)
    addIssueImpl(summary12, parent_issue_id, issue_type_id)
    sleep(1)
    addIssueImpl(summary13, parent_issue_id, issue_type_id)


def addNewTask():
    parent_issue_id = 12255779
    jira_issue_id = '(SB-2081)'
    summary1   = jira_issue_id + '現状調査'
    summary2   = jira_issue_id + '適用範囲調査'
    summary3   = jira_issue_id + '仕様検討'
    summary4   = jira_issue_id + '仕様レビュー'
    summary5   = jira_issue_id + 'ソース調査'
    summary6   = jira_issue_id + '仕様書作成'
    summary7   = jira_issue_id + '仕様書チームレビュー'
    summary8   = jira_issue_id + '仕様書全体レビュー'    
    summary9   = jira_issue_id + '試験仕様書作成'
    summary10  = jira_issue_id + '試験仕様書チームレビュー'
    summary11  = jira_issue_id + '試験仕様書全体レビュー'    
    summary12  = jira_issue_id + 'UI設計'
    summary13  = jira_issue_id + 'ロジック設計'
    summary14  = jira_issue_id + '設計レビュー'
    summary15  = jira_issue_id + '実装'
    summary16  = jira_issue_id + 'コードレビュー'
    summary17  = jira_issue_id + 'Verification'
    summary18  = jira_issue_id + '結合テスト'    

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
    print(summary14)
    print(summary15)
    print(summary16)
    print(summary17)
    print(summary18)

    issue_type_id = 714570

    addIssueImpl(summary1, parent_issue_id, issue_type_id)
    sleep(1)
    addIssueImpl(summary2, parent_issue_id, issue_type_id)
    sleep(1)
    addIssueImpl(summary3, parent_issue_id, issue_type_id)
    sleep(1)
    addIssueImpl(summary4, parent_issue_id, issue_type_id)
    sleep(1)
    addIssueImpl(summary5, parent_issue_id, issue_type_id)
    sleep(1)
    addIssueImpl(summary6, parent_issue_id, issue_type_id)
    sleep(1)
    addIssueImpl(summary7, parent_issue_id, issue_type_id)
    sleep(1)
    addIssueImpl(summary8, parent_issue_id, issue_type_id)
    sleep(1)
    addIssueImpl(summary9, parent_issue_id, issue_type_id)
    sleep(1)
    addIssueImpl(summary10, parent_issue_id, issue_type_id)
    sleep(1)
    addIssueImpl(summary11, parent_issue_id, issue_type_id)
    sleep(1)
    addIssueImpl(summary12, parent_issue_id, issue_type_id)
    sleep(1)
    addIssueImpl(summary13, parent_issue_id, issue_type_id)
    sleep(1)
    addIssueImpl(summary14, parent_issue_id, issue_type_id)
    sleep(1)
    addIssueImpl(summary15, parent_issue_id, issue_type_id)
    sleep(1)
    addIssueImpl(summary16, parent_issue_id, issue_type_id)
    sleep(1)
    addIssueImpl(summary17, parent_issue_id, issue_type_id)
    sleep(1)
    addIssueImpl(summary18, parent_issue_id, issue_type_id)

addNewTask()
#addDefectIssue()