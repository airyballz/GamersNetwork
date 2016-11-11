import web
games = web.Crawl()

def find_path_to_friend(network, user_A, user_B):
    # Proceed if both users are in network.
    if user_A in network and user_B in network:
        search = [user_A]
        path = [user_A]        
        while path:
            found = False
            nextuser = path[-1]
            links = network[nextuser]['linked']
            
            if user_B in links:
                path.append(user_B)
                return path

            for link in links:
                if link not in search:
                    path.append(link)
                    search.append(link)                
                    found = True
                    break

            if not found:
                path.pop()

    return None
#print games.page()
print find_path_to_friend(games.page(),'John','Jennie')
