from flask import render_template, request, flash, redirect, url_for, Blueprint
from datetime import datetime
from flask_login import UserMixin, login_user, logout_user, current_user, login_required
#luke new imports###########################################################
from .oauth import OAuthSignIn
from .models import User, Bodyweight, HangboardWerk, KampusWerkout, CircuitMoves, Routes, Blocs
from app import db
from .forms import KampusForm, HangboardForm, CircuitForm, BlocForm, BodyweightForm, RoutesForm

#luke new imports end#####################################################

views = Blueprint("", __name__)

###################################################################################################

# @views.route('/kampustest', methods=['GET', 'POST'])
# def function():
#     return render_template('KAMPUSWERK.html')

# @views.route("/test", methods=['GET'])
# def test():
#     return "This is a Test!"


@views.route('/', methods=["GET","POST"])
def index():
    return render_template('index.html')

@views.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('.index'))

@views.route('/authorize/<provider>')
def oauth_authorize(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('.index'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()

@views.route('/callback/<provider>')
def oauth_callback(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('.index'))
    oauth = OAuthSignIn.get_provider(provider)
    social_id, username, email = oauth.callback()
    if social_id is None:
        flash('Authentication failed.')
        return redirect(url_for('.index'))
    user = User.query.filter_by(social_id=social_id).first()
    if not user:
        user = User(social_id=social_id, nickname=username, email=email)
        db.session.add(user)
        db.session.commit()
    login_user(user, True)
    return redirect(url_for('.index'))
######################################################################################################################

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))


#############################################
############# VIEWS #########################
#############################################


@views.route("/circuits", methods=["GET", "POST"])
@login_required
def Circuit():
    form = CircuitForm()
    if form.validate_on_submit():
        timestamp=datetime.utcnow()

        circuitmove = CircuitMoves(current_user.nickname, request.form['numberofmoves'], request.form['intensity'], request.form['werktime'], request.form['comments'], request.form['grade'], timestamp, current_user.id)
        db.session.add(circuitmove)
        db.session.commit()
        flash('You have successfully logged your circuit')

    else:
        flash_errors(form)

    return render_template("circuits.html", title="Time to get strong", form=form, circuit=CircuitMoves.query.all())
##########################################################


@views.route("/hangboard", methods=["GET", "POST"])
@login_required
def Hangboard():
    form = HangboardForm()
    if form.validate_on_submit():
        timestamp=datetime.utcnow()
        werk = HangboardWerk(current_user.nickname, request.form['board'], request.form['holds_used'], request.form['reps'], request.form['sets'], request.form['setrest'], request.form['arm_used'], request.form['hangtime'], request.form['resttime'], request.form['weight_kg'], timestamp, current_user.id)
        db.session.add(werk)
        db.session.commit()
        return render_template("timerwerk.html", hangtime=request.form['hangtime'], resttime=request.form['resttime'], reps=request.form['reps'], sets = request.form['sets'], setrest=request.form['setrest'], arm_used = request.form['arm_used'])
    else:
        flash_errors(form)
    return render_template("hangboard.html", title="Time to get strong", form=form, hangboard=HangboardWerk.query.all())


#################################################################
@views.route("/climbing", methods=["GET", "POST"])
@login_required
def Climbing():
    form = RoutesForm()
    if form.validate_on_submit():
        timestamp=datetime.utcnow()

        routes = Routes(current_user.nickname, request.form['height'], request.form['intensity'], request.form['werktime'], request.form['grade'], request.form['angle'], request.form['venue'], request.form['style'], request.form['comments'],  timestamp, current_user.id)
        db.session.add(routes)
        db.session.commit()
        flash('You have successfully logged your route')

    else:
        flash_errors(form)

    return render_template("climbing.html", title="Time to get strong", form=form, routes=Routes.query.all())
##########################################################
@views.route("/bouldering", methods=["GET", "POST"])
@login_required
def Bouldering():
    form = BlocForm()
    if form.validate_on_submit():
        timestamp=datetime.utcnow()

        blocs = Blocs(current_user.nickname, request.form['intensity'], request.form['werktime'], request.form['grade'], request.form['angle'], request.form['venue'], request.form['style'], request.form['comments'],  timestamp, current_user.id)
        db.session.add(blocs)
        db.session.commit()
        flash('You have successfully logged your blocs')

    else:
        flash_errors(form)

    return render_template("bouldering.html", title="Time to get strong", form=form, blocs=Blocs.query.all())
##########################################################

@views.route("/profile", methods=["GET", "POST"])
@login_required
def Profile():

   
    return render_template("profile.html", kampus=KampusWerkout.query.filter_by(user_id=current_user.id).all(),
     hangboard=HangboardWerk.query.filter_by(user_id=current_user.id).all(),
         circuitmoves=CircuitMoves.query.filter_by(user_id=current_user.id).all(),
          routes=Routes.query.filter_by(user_id=current_user.id).all(),
           blocs=Blocs.query.filter_by(user_id=current_user.id).all() )

############################################################


@views.route("/kampus", methods=["GET", "POST"])
@login_required
def Kampus():
    if request.method == "POST":
        timestamp=datetime.utcnow()
        kampuswerkout = KampusWerkout(current_user.nickname, request.form['kampuslog'], timestamp, current_user.id)
        db.session.add(kampuswerkout)
        db.session.commit()
        return render_template("kampus.html", kampus=KampusWerkout.query.filter_by(user_id=current_user.id).all())
    return render_template("kampus.html") #, kampus=KampusWerkout.query.all())


############################################################

#part of the hangboard pages
@views.route("/timerwerk", methods=["GET","POST"])
def timer():
    return render_template("timerwerk.html")


#cool round timer i might use#    

@views.route("/intervaltimer", methods=["GET","POST"])
def intervals():
    return render_template("intervaltimer.html")


#########################################
#need to create weight.html page~ 
@views.route("/weight", methods=["GET", "POST"])
@login_required
def Weight():
    form = BodyweightForm()
    if form.validate_on_submit():
        timestamp=datetime.utcnow()
        bodyweight = Bodyweight(current_user.nickname, request.form["bodyweight_kg"], request.form["notes"], timestamp, current_user.id)
        db.session.add(bodyweight)
        db.session.commit()
        flash('You have successfully logged your weight')
    else:
        flash_errors(form)
    return render_template("weight.html", form=form, bodyweight=Bodyweight.query.all())