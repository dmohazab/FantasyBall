from API.helpers.create_model_app import create_model_app
import os

# Creating a new application instance for this modularized API section, an app is made for each so that it can be
# assigned a unique blueprint
db_player_data = create_model_app(os.environ['PLAYER_DATA_BIND'])
TABLE_NAME = 'playerdata'


# Table definitions for the playerdata table, showing the columns and what datatype they are
class playerdata(db_player_data.Model):
    __tablename__ = TABLE_NAME

    id = db_player_data.Column(db_player_data.Integer, primary_key=True, unique=True)
    name = db_player_data.Column(db_player_data.Text, unique=False)
    age = db_player_data.Column(db_player_data.Text, unique=False)
    date = db_player_data.Column(db_player_data.Text, unique=False)
    tm = db_player_data.Column(db_player_data.Text, unique=False)
    opp = db_player_data.Column(db_player_data.Text, unique=False)
    gs = db_player_data.Column(db_player_data.Integer, unique=False)
    mp = db_player_data.Column(db_player_data.Integer, unique=False)
    fg = db_player_data.Column(db_player_data.Integer, unique=False)
    fga = db_player_data.Column(db_player_data.Integer, unique=False)
    fg_p = db_player_data.Column(db_player_data.Float, unique=False)
    twop = db_player_data.Column(db_player_data.Integer, unique=False)
    twopa = db_player_data.Column(db_player_data.Integer, unique=False)
    twop_p = db_player_data.Column(db_player_data.Float, unique=False)
    threep = db_player_data.Column(db_player_data.Integer, unique=False)
    threepa = db_player_data.Column(db_player_data.Integer, unique=False)
    threep_p = db_player_data.Column(db_player_data.Float, unique=False)
    ft = db_player_data.Column(db_player_data.Integer, unique=False)
    fta = db_player_data.Column(db_player_data.Integer, unique=False)
    ft_p = db_player_data.Column(db_player_data.Float, unique=False)
    orb = db_player_data.Column(db_player_data.Integer, unique=False)
    drb = db_player_data.Column(db_player_data.Integer, unique=False)
    trb = db_player_data.Column(db_player_data.Integer, unique=False)
    ast = db_player_data.Column(db_player_data.Integer, unique=False)
    stl = db_player_data.Column(db_player_data.Integer, unique=False)
    blk = db_player_data.Column(db_player_data.Integer, unique=False)
    tov = db_player_data.Column(db_player_data.Integer, unique=False)
    pf = db_player_data.Column(db_player_data.Integer, unique=False)
    pts = db_player_data.Column(db_player_data.Integer, unique=False)
    gmsc = db_player_data.Column(db_player_data.Float, unique=False)

    def __init__(self, name, age, date, tm, opp, gs, mp, fg, fga, fg_p, twop, twopa, twop_p, threep, threepa, threep_p,
                 ft, fta, ft_p, orb, drb, trb, ast, stl, blk, tov, pf, pts, gmsc):
        self.name = name
        self.age = age
        self.date = date
        self.tm = tm
        self.opp = opp
        self.gs = gs
        self.mp = mp
        self.fg = fg
        self.fga = fga
        self.fg_p = fg_p
        self.twop = twop
        self.twopa = twopa
        self.twop_p = twop_p
        self.threep = threep
        self.threepa = threepa
        self.threep_p = threep_p
        self.ft = ft
        self.fta = fta
        self.ft_p = ft_p
        self.orb = orb
        self.drb = drb
        self.trb = trb
        self.ast = ast
        self.stl = stl
        self.blk = blk
        self.tov = tov
        self.pf = pf
        self.pts = pts
        self.gmsc = gmsc