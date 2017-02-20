from flask_wtf import Form
from wtforms import StringField, BooleanField, IntegerField, SelectField, RadioField,  PasswordField, DecimalField, validators

from wtforms.validators import DataRequired, Required, InputRequired

class HangboardForm(Form):
    board = SelectField('Board Used', default='BeastMaker2000', choices=[('BeastMaker2000' , 'BeastMaker2000'), ('BeastMaker1000', 'BeastMaker1000'), ('KampusRung' , 'KampusRung'), ('OtherBoard', 'OtherBoard')])
    holds_used =SelectField('Select Hold', default=6, choices=[('1' , '1'), ('2', '2'), ('3' , '3'), ('4', '4'), ('5', '5'), ('6' , '6'), ('7', '7'), ('8' , '8'), ('9', '9'), ('10', '10'), ('11' , '11'), ('12', '12'), ('13' , '13'), ('14', '14'), ('15', '15')])
    reps = SelectField('Repetitions', default=6, choices=[('1' , '1'), ('2', '2'), ('3' , '3'), ('4', '4'), ('5', '5'), ('6' , '6'), ('7', '7'), ('8' , '8'), ('9', '9'), ('10', '10'), ('11' , '11'), ('12', '12'), ('13' , '13'), ('14', '14'), ('15', '15')])
    sets = SelectField('Sets', default=1, choices=[('1' , '1'), ('2', '2'), ('3' , '3'), ('4', '4'), ('5', '5'), ('6' , '6'), ('7', '7'), ('8' , '8'), ('9', '9'), ('10', '10'), ('11' , '11'), ('12', '12'), ('13' , '13'), ('14', '14'), ('15', '15')])
    setrest = IntegerField('Setrest (secs)', default=0, validators=[InputRequired()])

    arm_used = SelectField('Arm Used', default='Both', choices=[('Both' , 'Both'), ('Left', 'Left'), ('Right', 'Right')])
    hangtime = SelectField('Hangtime (secs)', default='7', choices=[('1' , '1'), ('2', '2'), ('3' , '3'), ('4', '4'), ('5', '5'), ('6' , '6'), ('7', '7'), ('8' , '8'), ('9', '9'), ('10', '10'), ('11' , '11'), ('12', '12'), ('13' , '13'), ('14', '14'), ('15', '15'), ('16' , '16'), ('17', '17'), ('18' , '18'), ('19', '19'), ('20', '20'),  ('21' , '21'), ('22', '22'), ('23' , '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28' , '28'), ('29', '29'), ('30', '30')])
    resttime = IntegerField('Rest (secs)', [validators.required()])
    weight_kg = IntegerField('Assist -+kg', default=0, validators=[InputRequired()])

class KampusForm(Form):
    hand = SelectField('Lead Arm', default='Right', choices=[('Both' , 'Both'), ('Left', 'Left'), ('Right', 'Right')])
    rung1 = BooleanField('rung1', default=False)
    rung2 = BooleanField('rung2', default=False)
    rung3 = BooleanField('rung3', default=False)
    rung4 = BooleanField('rung4', default=False)
    rung5 = BooleanField('rung5', default=False)
    rung6 = BooleanField('rung6', default=False)
    rung7 = BooleanField('rung7', default=False)
    rung8 = BooleanField('rung8', default=False)
    rung9 = BooleanField('rung9', default=False)

class BodyweightForm(Form):
    bodyweight_kg = DecimalField('bodyweight in kg', [validators.DataRequired()])
    notes = StringField('diet, mood notes', [validators.DataRequired()])

class CircuitForm(Form):
    numberofmoves = SelectField('Total Moves', default=40, choices=[('1' , '1'), ('2', '2'), ('3' , '3'), ('4', '4'), ('5', '5'), ('6' , '6'), ('7', '7'), ('8' , '8'), ('9', '9'), ('10', '10'), ('11' , '11'), ('12', '12'), ('13' , '13'), ('14', '14'), ('15', '15'), ('16' , '16'), ('17', '17'), ('18' , '18'), ('19', '19'), ('20', '20'),  ('21' , '21'), ('22', '22'), ('23' , '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28' , '28'), ('29', '29'), ('30', '30'), ('31' , '31'), ('32', '32'), ('33' , '33'), ('34', '34'), ('35', '35'), ('36' , '36'), ('37', '37'), ('38' , '38'), ('39', '39'), ('40', '40'), ('50', '50'), ('51' , '51'), ('52', '52'), ('53' , '53'), ('54', '54'), ('55', '55'), ('56' , '56'), ('57', '57'), ('58' , '58'), ('59', '59'), ('60', '60')])
    intensity = SelectField('Intensity 1-5', default='3', choices=[('1' , '1'), ('2', '2'), ('3' , '3'), ('4', '4'), ('5', '5')])
    grade = SelectField('Sports Grade', default='7a', choices=[('5', '5'), ('5+', '5+'), ('6a', '6a'), ('6a+', '6a+'), ('6b', '6b'), ('6b+', '6b+'), ('6c', '6c'), ('6c+', '6c+'), ('7a', '7a'), ('7a+', '7a+'), ('7b', '7b'), ('7b+', '7b+'), ('7c', '7c'), ('7c+', '7c+'), ('8a', '8a'), ('8a+', '8a+'), ('8b', '8b')])
    werktime = SelectField('Time (mins)', default=5, choices=[('1' , '1'), ('2', '2'), ('3' , '3'), ('4', '4'), ('5', '5'), ('6' , '6'), ('7', '7'), ('8' , '8'), ('9', '9'), ('10', '10')])
    comments = StringField('Enter Comments')

class RoutesForm(Form):
    height = SelectField('Height (m)', default='10',  choices=[('1' , '1'), ('2', '2'), ('3' , '3'), ('4', '4'), ('5', '5'), ('6' , '6'), ('7', '7'), ('8' , '8'), ('9', '9'), ('10', '10'), ('11' , '11'), ('12', '12'), ('13' , '13'), ('14', '14'), ('15', '15'), ('16' , '16'), ('17', '17'), ('18' , '18'), ('19', '19'), ('20', '20'), ('21' , '21'), ('22', '22'), ('23' , '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28' , '28'), ('29', '29'), ('30', '30'), ('30+' , '30+')])
    intensity = SelectField('Intensity 1-5', default='3', choices=[('1' , '1'), ('2', '2'), ('3' , '3'), ('4', '4'), ('5', '5')])
    werktime = SelectField('Time (mins)', default='5', choices=[('1' , '1'), ('2', '2'), ('3' , '3'), ('4', '4'), ('5', '5'), ('6' , '6'), ('7', '7'), ('8' , '8'), ('9', '9'), ('10', '10'), ('11' , '11'), ('12', '12'), ('13' , '13'), ('14', '14'), ('15', '15'), ('16' , '16'), ('17', '17'), ('18' , '18'), ('19', '19'), ('20', '20'), ('21' , '21'), ('22', '22'), ('23' , '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28' , '28'), ('29', '29'), ('30', '30'), ('30+' , '30+')])
    grade = SelectField('Sports Grade', default='7a', choices=[('5', '5'), ('5+', '5+'), ('6a', '6a'), ('6a+', '6a+'), ('6b', '6b'), ('6b+', '6b+'), ('6c', '6c'), ('6c+', '6c+'), ('7a', '7a'), ('7a+', '7a+'), ('7b', '7b'), ('7b+', '7b+'), ('7c', '7c'), ('7c+', '7c+'), ('8a', '8a'), ('8a+', '8a+'), ('8b', '8b')])
    angle = SelectField('Wall Angle', default='vertical', choices=[('slab' , 'slab'), ('vertical', 'vertical'), ('15' , '15 degrees'), ('30', '30 degrees'), ('45', '45 degrees'), ('roof', 'roof')])
    venue = SelectField('Venue Type', default='indoor', choices=[('indoors' , 'indoors'), ('outdoors', 'outdoors')])
    style = SelectField('Ascent Style', default='onsight', choices=[('onsight', 'onsight'), ('flash', 'flash'), ('redpoint', 'redpoint'), ('worked', 'worked/rested'), ('toprope', 'toprope')])
    comments = StringField('Enter Comments')

class BlocForm(Form):
    intensity = SelectField('Intensity 1-5', default='3', choices=[('1' , '1'), ('2', '2'), ('3' , '3'), ('4', '4'), ('5', '5')])
    werktime = SelectField('Time (mins)', default='2', choices=[('1' , '1'), ('2', '2'), ('3' , '3'), ('4', '4'), ('5', '5'), ('6' , '6'), ('7', '7'), ('8' , '8'), ('9', '9'), ('10', '10')])
    grade = SelectField('Font Boulder', choices=[('4', '4'), ('5', '5'), ('5+', '5+'), ('6a', '6a'), ('6a+', '6a+'), ('6b', '6b'), ('6b+', '6b+'), ('6c', '6c'), ('6c+', '6c+'), ('7a', '7a'), ('7a+', '7a+'), ('7b', '7b'), ('7b+', '7b+'), ('7c', '7c'), ('7c+', '7c+'), ('8a', '8a'), ('8a+', '8a+'), ('8b', '8b')])
    angle = SelectField('Wall Angle', default='vertical', choices=[('slab' , 'slab'), ('vertical', 'vertical'), ('15' , '15 degrees'), ('30', '30 degrees'), ('45', '45 degrees'), ('roof', 'roof')])
    venue = SelectField('Venue Type', default='indoor', choices=[('indoors' , 'indoors'), ('outdoors', 'outdoors')])
    style = SelectField('Ascent Style', default='onsight', choices=[('onsight', 'onsight'), ('flash', 'flash'), ('redpoint', 'redpoint'), ('worked', 'worked/rested')])
    comments = StringField('Enter Comments')