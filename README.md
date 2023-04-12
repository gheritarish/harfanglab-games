# HLgames
This is a small project made in less than 2 hours for an interview.

It is to be noted that this was my first try at django and django restful, so I hadn't the time to
add some of the features I wanted:

* Link a game to a platform on which it can be played
* Add extensive tests
* Add a linting configuration, though this project is linted with ruff and black

## Run it
You can simply run it by:

```shell
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd hlgames
python manage.py migrate
python manage.py createsuperuser --email admin@example.com --username admin
python manage.py runserver
```

You will need the admin account to link games to their platform directly in the database, as this
cannot be done by the API by lack of time and knowledge of the chosen framework.

## Current features
Almost none? You can list the games by calling `games`, adding the potential `name` and `ratings`
filters, as follow: `/games?ratings=19`

You can POST or PUT a game there, and you can list individual games.

The same is true for platforms, that you can list using `/platforms`, and POST on the same URL.

## Known bugs
Too many.

* You cannot link a game to its platform via the API. It would require an API such as
  `/game/platform` taking a game id and platform name in the json form.
* The filtering is strict, you cannot order by a field or list all games with ratings of 15 or more
  (for instance).
* Where are the tests? By lack of time, I might have no tests or very few, which is bad. I would
  have liked to test at least the following:
  * Listing of games
  * Filtering using a range (or at least more than / less than), such as `games?ratings=15--` to
    list all games with a rating of 15 or more.

## Conclusion
Well, all that to say I am not very satisfied with what I could do in such a limited time.

## Tests
The tests were committed after the two hours, so feel free to discard them.
