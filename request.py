import requests

print('\nUNIGRAM requests\n')
text={"description":"hollandrad 28 zoll gangschaltung"}
print("description {}".format(text["description"]))
resp = requests.post('http://127.0.0.1:5555/request', json=text)
if resp.status_code != 200:
    print("nix da", resp.status_code)
    exit()
print('category {}'.format(resp.json()["category"]))
print('inference time: ', resp.json()["inf_time"], " microseconds")

text={"description":"hgg wam bauknecht wa"}
print("description {}".format(text["description"]))
resp = requests.post('http://127.0.0.1:5555/request', json=text)
if resp.status_code != 200:
    print("nix da", resp.status_code)
    exit()
print('category {}'.format(resp.json()["category"]))
print('inference time: ', resp.json()["inf_time"], " microseconds")

text={"description":"sandisk 32gb ultra fit 3.0 gb"}
print("description {}".format(text["description"]))
resp = requests.post('http://127.0.0.1:5555/request', json=text)
if resp.status_code != 200:
    print("nix da", resp.status_code)
    exit()
print('category {}'.format(resp.json()["category"]))
print('inference time: ', resp.json()["inf_time"], " microseconds")

text={"description":"program siemens"}
print("description {}".format(text["description"]))
resp = requests.post('http://127.0.0.1:5555/request', json=text)
if resp.status_code != 200:
    print("nix da", resp.status_code)
    exit()
print('category {}'.format(resp.json()["category"]))
print('inference time: ', resp.json()["inf_time"], " microseconds")

print('\nDEEP LEARNING requests\n')
text={"description":"hollandrad 28 zoll gangschaltung"}
print("description {}".format(text["description"]))
resp = requests.post('http://127.0.0.1:5555/request_dl', json=text)
if resp.status_code != 200:
    print("nix da", resp.status_code)
    exit()
print('category {}'.format(resp.json()["category"]))
print('inference time: ', resp.json()["inf_time"], " microseconds")

text={"description":"hgg wam bauknecht wa"}
print("description {}".format(text["description"]))
resp = requests.post('http://127.0.0.1:5555/request_dl', json=text)
if resp.status_code != 200:
    print("nix da", resp.status_code)
    exit()
print('category {}'.format(resp.json()["category"]))
print('inference time: ', resp.json()["inf_time"], " microseconds")

text={"description":"sandisk 32gb ultra fit 3.0 gb"}
print("description {}".format(text["description"]))
resp = requests.post('http://127.0.0.1:5555/request_dl', json=text)
if resp.status_code != 200:
    print("nix da", resp.status_code)
    exit()
print('category {}'.format(resp.json()["category"]))
print('inference time: ', resp.json()["inf_time"], " microseconds")

text={"description":"program siemens"}
print("description {}".format(text["description"]))
resp = requests.post('http://127.0.0.1:5555/request_dl', json=text)
if resp.status_code != 200:
    print("nix da", resp.status_code)
    exit()
print('category {}'.format(resp.json()["category"]))
print('inference time: ', resp.json()["inf_time"], " microseconds")
