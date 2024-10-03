def solution(players, callings):
    player_ranks = {player: rank for rank, player in enumerate(players)}
    
    for called_player in callings:
        current_rank = player_ranks[called_player]
        
        player_ahead = players[current_rank - 1]
            
        players[current_rank - 1], players[current_rank] = players[current_rank], players[current_rank - 1]
            
        player_ranks[called_player] = current_rank - 1
        player_ranks[player_ahead] = current_rank
    
    return players