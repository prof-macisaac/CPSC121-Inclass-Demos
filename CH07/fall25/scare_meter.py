def update_scream_meter_with_stats(records):
    """
    Args:
        records: list of (room, screams) tuples

    Returns:
        (updated_list, avg, mn, mx)
        - updated_list: a new copy of records with "Hall of Mirrors" removed
                        and "Witch's Kitchen" screams set to 85 (keep position)
        - avg: float average of screams in updated_list
        - mn: minimum screams value
        - mx: maximum screams value
    """

    
    updated_list = []
    for ind in range(len(records)):
        updated_list.append(records[ind])
    print(updated_list)

    # remove hall of mirrors
    updated_list.remove(("Hall of Mirrors", 94))

    # update witch's kitchen
    witch_index = updated_list.index(("Witch's Kitchen", 91))
    updated_list[witch_index] = ("Witch's Kitchen", 85)

    # calculate vals
    # version 1
    mn = updated_list[0][1]
    mx = updated_list[0][1]
    sm = 0
    av = None
    for ind in range(len(updated_list)):
        val = updated_list[ind][1]
        sm += val
        if val < mn:
            # value is less than minimum
            mn = val
        if val > mx:
            # value is greater than maximum
            mx = val
    av = sm/len(updated_list)

    # version 2
    scream_scores = []
    for ind in range(len(updated_list)):
        scream_scores.append(updated_list[ind][1])

    mn = min(scream_scores)
    mx = max(scream_scores)
    av = sum(scream_scores)/ len(scream_scores)
    return updated_list, av, mn, mx

def main():
    scream_meter = [
        ('Foyer of Fog', 88),
        ('Hall of Mirrors', 94),
        ('Basement Chains', 73),
        ("Witch's Kitchen", 91),
        ('Attic Shadows', 85),
        ('Crypt Corridor', 90),
        ('Spider Den', 42)
    ]
    updated_scream_meter, avg_scream, min_scream, max_scream = update_scream_meter_with_stats(scream_meter)

    print(scream_meter)
    print(updated_scream_meter)
    print(avg_scream)
    print(min_scream)
    print(max_scream)

if __name__ == "__main__":
    main() 