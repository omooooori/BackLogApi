#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from time import sleep

def createIssueImpl(summary, parent_issue_id, issue_type_id):
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


def createIssue(summary_list, parent_issue_id, issue_type_id):
    for summary in summary_list:
        print(summary)
        createIssueImpl(summary, parent_issue_id, issue_type_id)
        sleep(1)


def addDefectIssue():
    parent_issue_id = 12449537
    jira_issue_id = '(SB-2044)'
    issue_type_id = 204076

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

    summary_list = [
        summary1, 
        summary2, 
        summary3, 
        summary4, 
        summary5, 
        summary6, 
        summary7, 
        summary8, 
        summary9, 
        summary10, 
        summary11, 
        summary12, 
        summary13
    ]
    createIssue(summary_list, parent_issue_id, issue_type_id)


def addNewTask():
    parent_issue_id = 12255779
    jira_issue_id = '(SB-2081)'
    issue_type_id = 714570

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

    summary_list = [
        summary1, 
        summary2, 
        summary3, 
        summary4, 
        summary5, 
        summary6, 
        summary7, 
        summary8, 
        summary9, 
        summary10, 
        summary11, 
        summary12, 
        summary13, 
        summary14, 
        summary15, 
        summary16, 
        summary17, 
        summary18
    ]
    createIssue(summary_list, parent_issue_id, issue_type_id)


addNewTask()
#addDefectIssue()