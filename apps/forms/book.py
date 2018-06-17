from wtforms import Form
from wtforms import StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=50)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)