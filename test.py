# import re


# def extract_parameters(url):
#     pattern = re.compile(r'(\w+)=([^&]+)')
#     matches = pattern.findall(url)
#     parameters = {key: value for key, value in matches}
#     return parameters


# def getResponses(valid_auth_tokens, requests: list):
#     tokens = valid_auth_tokens
#     res = ["VALID"]
#     for i in requests:
#         param = extract_parameters(i[1])
#         if param["token"] in tokens:
#             for key, val in param.items():
#                 if key != "token":
#                     res.append(key)
#                     res.append(val)
#         else:
#             return "INVALID"
#     return [",".join(res)]

# # # #     ...


# # # def strokesRequired(picture):
# # #     def dfs(row, col, group_id):
# # #         if row < 0 or row >= rows or col < 0 or col >= cols:
# # #             return
# # #         if visited[row][col] or picture[row][col] != current_char:
# # #             return
# # #         visited[row][col] = True
# # #         groups[row][col] = group_id
# # #         for dr, dc in directions:
# # #             new_row, new_col = row + dr, col + dc
# # #             dfs(new_row, new_col, group_id)
# # #     rows = len(picture)
# # #     cols = len(picture[0])
# # #     visited = [[False for _ in range(cols)] for _ in range(rows)]
# # #     groups = [[0 for _ in range(cols)] for _ in range(rows)]
# # #     group_id = 0
# # #     directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# # #     for row in range(rows):
# # #         for col in range(cols):
# # #             if not visited[row][col]:
# # #                 current_char = picture[row][col]
# # #                 group_id += 1
# # #                 dfs(row, col, group_id)

# # #     return group_id


# # # # Example picture
# # # picture = [
# # #     ['a', 'a', 'a', 'b', 'b'],
# # #     ['a', 'a', 'a', 'a', 'b'],
# # #     ['a', 'a', 'a', 'c', 'b']
# # # ]

# print(*getResponses(["wdjshc3874e3n"], [
#       ["POST", "https://www.example.com/?token=wdjshc3874e3n&name=alex&age=25"]]))
# # def find_groups(picture):
# #     def dfs(row, col, group_id):
# #         if row < 0 or row >= rows or col < 0 or col >= cols:
# #             return
# #         if visited[row][col] or picture[row][col] != current_char:
# #             return

# #         visited[row][col] = True
# #         groups[row][col] = group_id

# #         for dr, dc in directions:
# #             new_row, new_col = row + dr, col + dc
# #             dfs(new_row, new_col, group_id)

# #     rows = len(picture)
# #     cols = len(picture[0])

# #     visited = [[False for _ in range(cols)] for _ in range(rows)]
# #     groups = [[0 for _ in range(cols)] for _ in range(rows)]
# #     group_id = 0

# #     directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# #     for row in range(rows):
# #         for col in range(cols):
# #             if not visited[row][col]:
# #                 current_char = picture[row][col]
# #                 group_id += 1
# #                 dfs(row, col, group_id)

# #     return group_id

# # # Example picture as a list of strings
# # picture = [
# #     'aaaab',
# #     'aaaaa',
# #     'aabcb'
# # ]

# # number_of_groups = find_groups(picture)
# # print(f"Number of groups: {number_of_groups}")

# # def strokesRequired(picture):
# #     def dfs(row, col, group_id):
# #         if row < 0 or row >= rows or col < 0 or col >= cols:
# #             return
# #         if visited[row][col] or picture[row][col] != current_char:
# #             return
# #         visited[row][col] = True
# #         groups[row][col] = group_id
# #         for dr, dc in directions:
# #             new_row, new_col = row + dr, col + dc
# #             dfs(new_row, new_col, group_id)
# #     if not picture or not picture[0]:
# #         return 0 
# #     rows = len(picture)
# #     cols = len(picture[0])
# #     visited = [[False for _ in range(cols)] for _ in range(rows)]
# #     groups = [[0 for _ in range(cols)] for _ in range(rows)]
# #     group_id = 0
# #     directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# #     for row in range(rows):
# #         for col in range(cols):
# #             if not visited[row][col]:
# #                 current_char = picture[row][col]
# #                 group_id += 1
# #                 dfs(row, col, group_id)

# #     return group_id

# # # Example Usage:
# # picture = [
# #     'aaaab',
# #     'aaaaa',
# #     'aabcb'
# # ]

# # try:
# #     number_of_groups = find_groups(picture)
# #     print(f"Number of groups: {number_of_groups}")
# # except ValueError as e:
# #     print(f"Error: {e}")

class A(Exception):
    pass
class B(A):pass
class C(B):pass

for i in [A,B,C]:
    try:
        raise(i)
    except A:print(A)
    except B:print(B)
    except C:print(C)