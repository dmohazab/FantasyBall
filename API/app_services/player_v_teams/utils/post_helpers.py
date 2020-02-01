from ..Models.playerdata import playerdata


def create_player_post(json_body, db):
    row_count = 0
    for row in json_body:
        name = row['name']
        age = row['age']
        date = row['date']
        tm = row['tm']
        opp = row['opp']
        gs = row['gs']
        mp = row['mp']
        fg = row['fg']
        fga = row['fga']
        fg_p = row['fg_p']
        twop = row['twop']
        twopa = row['twopa']
        twop_p = row['twop_p']
        threep = row['threep']
        threepa = row['threepa']
        threep_p = row['threep_p']
        ft = row['ft']
        fta = row['fta']
        ft_p = row['ft_p']
        orb = row['orb']
        drb = row['drb']
        trb = row['trb']
        ast = row['ast']
        stl = row['stl']
        blk = row['blk']
        tov = row['tov']
        pf = row['pf']
        pts = row['pts']
        gmsc = row['gmsc']

        new_row = playerdata(name, age, date, tm, opp, gs, mp, fg, fga, fg_p, twop, twopa, twop_p, threep, threepa, threep_p,
                 ft, fta, ft_p, orb, drb, trb, ast, stl, blk, tov, pf, pts, gmsc)
        db.session.add(new_row)
        row_count += 1
    return row_count