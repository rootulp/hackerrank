_num_english_subscribers = int(input())
english_subscribers = set(map(int, input().split(" ")))
_num_french_subscribers = int(input())
french_subscribers = set(map(int, input().split(" ")))

print(len(english_subscribers ^ french_subscribers))
