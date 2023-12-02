# Title: 
# Difficulty: Medium
# Problem: 

# using simple dictionary
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        account_dict = {}

        for idx, account in enumerate(accounts):
            if account[0] in account_dict:
                curr_emails = set(account[1:])
                change = False
                old_lists = []
                for email_list in account_dict[account[0]]:
                    for email in curr_emails:
                        if email in email_list:
                            curr_emails = email_list | curr_emails
                            old_lists.append(email_list)
                            change = True
                            break
                if change:
                    for email_list in old_lists:
                        account_dict[account[0]].remove(email_list)
                account_dict[account[0]].append(curr_emails)
            else:
                account_dict[account[0]] = [set(account[1:])]
        
        res = []
        for name in account_dict:
            for email_list in account_dict[name]:
                emails = list(email_list)
                emails.sort()
                res.append([name] + emails)

        return res

  # using graph
  from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)
        visited = set()

        for account in accounts:
            first_email = account[1]
            graph[first_email]
            for i in range(2, len(account)):
                graph[first_email].append(account[i])
                graph[account[i]].append(first_email)

        def dfs(email: str, path: list):
            visited.add(email)
            path.append(email)

            for child in graph[email]:
                if not child in visited:
                    dfs(child, path)

        result = []
        for account in accounts:
            for i in range(1, len(account)):
                if not account[i] in visited:
                    path = []
                    dfs(account[i], path)
                    result.append([account[0]] + sorted(path))

        return result
