def get_friends_ids(api, user_id):
    friends = api.friends.get(user_id=user_id, v = '5.68')
    friends_ids = friends['items']
    
    return friends_ids

def get_user_groups(api, user_id, moder=True, only_open=True):
    kwargs = {'user_id' : user_id,
              'v' : '5.68'  
              }
    
    if moder == True:
        kwargs['filter'] = 'moder'
    if only_open == True:
        kwargs['extended'] = 1
        kwargs['fields'] = ['is_closed']
    
    groups = api.groups.get(**kwargs)
    groups_refined = []
    for group in groups['items']:
        cond_check = (only_open and group['is_closed'] == 0) or not only_open
        if cond_check:
            refined = {}
            refined['id'] = group['id'] * (-1)
            refined['name'] = group['name']
            groups_refined.append(refined)
    
    return groups_refined

def get_n_posts_text(api, group_id, n_posts=50):
    wall_contents = api.wall.get(owner_id = group_id, count=n_posts, v = '5.68')
    wall_contents = wall_contents['items']
    text = ''
    for post in wall_contents:
        text += post['text'] + ' '
    return text