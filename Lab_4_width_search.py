from collections import deque

# Информация о людях и их связях
people_data = {
    "Alice": {"profession": "Engineer"},
    "Bob": {"profession": "Chef"},
    "Charlie": {"profession": "Doctor"},
    "David": {"profession": "Teacher"}
}

# Информация о друзьях каждого человека, включая их профессии
friends_data = {
    "Alice": {"friends": [{"name": "Eve", "profession": "Artist"}, {"name": "Grace", "profession": "Driver"}]},
    "Bob": {"friends": [{"name": "Frank", "profession": "Engineer"}, {"name": "Helen", "profession": "Artist"}]},
    "Charlie": {"friends": [{"name": "Ivy", "profession": "Teacher"}, {"name": "Jack", "profession": "Chef"}]},
    "David": {"friends": [{"name": "Kate", "profession": "Doctor"}, {"name": "Leo", "profession": "Engineer"}]}
}

def bfs_search(start_person, target_profession):
    # Очередь для BFS
    queue = deque()
    # Множество для отслеживания посещенных людей
    visited = set()

    # Начинаем с первого человека
    queue.append(start_person)
    visited.add(start_person)

    while queue:
        current_person = queue.popleft()

        # Проверяем, существует ли вершина в people_data
        if current_person in people_data:
            profession = people_data[current_person]["profession"]

            # Проверяем, соответствует ли профессия
            if profession == target_profession:
                return current_person  # Нашли человека с нужной профессией

            # Добавляем всех друзей человека в очередь, если они еще не были посещены
            if current_person in friends_data:
                for friend_info in friends_data[current_person]["friends"]:
                    friend_name = friend_info["name"]

                    if friend_name not in visited:
                        queue.append(friend_name)
                        visited.add(friend_name)

                        # Проверяем профессию друга
                        friend_profession = friend_info.get("profession", "")
                        if friend_profession == target_profession:
                            return friend_name  # Нашли друга с нужной профессией

    return None  # Не нашли человека с нужной профессией

# Ищем повара среди всех друзей и их друзей, и так далее
for person in people_data.keys():
    result = bfs_search(person, "Chef")

    if result:
        print(f"Найден повар: {result}")
    else:
        print(f"Повар не найден.")
