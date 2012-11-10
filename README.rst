======
notset
======

A Do-Not-Care Value for Python

Let's Talk About Kwargs
=======================

It's easy to take for granted, but one of the most elegant aspects of Python
is its handling of functional keyword arguments (kwargs). This one construct
provides:

    1. A way to specify parameters without having to know its position in the
       argument list

    2. Automatic checking of expected parameters

    3. An elegant way to specify parameter defaults

    4. A meaningful, self-documenting function signature

Most of the time kwargs work flawlessly; but there are a few cases where
their use becomes tricky.

I'm going to talk about that problem, show one common anti-pattern that
attempts to fix it, and then propose an alternate approach that retains all of
the benefits mentioned above at the cost of introducing a new concept to
Python, the ``NotSet`` singleton.

Problem, What Problem?
======================

Let's start off with an example. Suppose you have a function which takes a
person and allows you to update the person's name, age, both, or neither.
Naively, you might write that function as something like::

    def update(person, name=None, age=None):
        person.name = name
        person.age = age

Now let's call this function, but only update the person's age::

    > person = Person(name='Alice', age=32)
    > update(person, age=33)
    > person.age
    33
    > person.name
    None

Notice that the code correctly set the age but, unexpectedly from the caller's
point-of-view, also set the name to ``None``.  Not what we intended.

The problem here is that ``None`` can't be used to both represent a valid value
and at the same time we used to represent a do-not-care condition.

Realizing we need a way to differentiate these two conditions, we modify the
code slightly::

    def update(person, **kwargs):
        for k, v in kwargs.items():
            setattr(person, k, v)

Here we're using the presence or absence of the key in the kwargs dict to
represent the do-not-care condition and the value of ``None`` is solely reserved
for actually setting the attribute to ``None`` (pretty reasonable, huh?).

Let's call this new version of ``update`` again::

    > person = Person(name='Alice', age=32)
    > update(person, age=33)
    > person.age
    33
    > person.name
    'Alice'

The method behaved exactly as we expected. And from my experience, many
developers stop here because It Just Works. But it comes at a cost: we no
longer have expected kwarg checking (benefit #2), no elegant way of setting
default parameters (benefit #3), and we've lost our meaningful function
signature (benefit #4). For these reasons, I consider this an anti-pattern and
propose a a different approach.

None More None
==============

To retain the benefits of explicit kwargs, we need a way for the *value* of
the keyword to differentiate between the do-not-care condition and a valid
value. As we've seen above, ``None`` isn't good enough since ``None`` is a
perfectly reasonable value for many attributes.

Instead we need to create a new value, a singleton like ``None`` that can
represent this case which I call ``NotSet``. With it, our function becomes::

    NotSet = object()

    def update(person, name=NotSet, age=NotSet):
        if name is not NotSet:
            person.name = name

        if age is not NotSet:
            person.age = age


Leaving aside the double-negative soundingness of 'not not-set', we end up
with code that behaves exactly as we'd expect when called, but also preserves
the benefits of explicit kwargs::

    update(person, age=33)      # Just set the age to 33
    update(person, name=None)   # Set the name to None
    update(person)              # Doesn't update any attributes
    update(person, foo=bar)     # Raises a TypeError because foo isn't an
                                # expected kwargs (benefit #2)


So What's The Catch?
====================

So, solving our default kwarg problem, we've gone ahead an published our
library containing our ``update`` function. Now suppose that someone comes along
and wants to use our library. First of all, they'll be appreciative of our
usage of explicit kwargs--once they get past the unusual looking ``NotSet``
defaults.

However, when they go to use it, they might do something like::

    NotSet = object()

    def update_with_email(person, name=NotSet, age=NotSet):
        update(person, name=name, age=age)
        send_email(person)

    > person = Person(name='Alice', age=32)
    > update_with_email(age=33)
    > person.age
    33
    > person.name
    <object object at 0x105ae2080>


As you can see, ``person.name`` has ended up with the value of ``NotSet``.  The
problem here is that caller's ``NotSet`` instance is different from the
libraries ``NotSet`` instance, so they don't compare as identical.

What we'd like is a way to define a single global singleton that represents
this do-not-care condition across all Python packages, in the same way that
``None`` is identical no matter where it's used.


Introducing...
==============

This Python module aims to solve this problem by defining the one-and-only
``NotSet`` instance, shareable between all packages on the system.

To be clear, just because a library uses ``notset``, it doesn't mean the
calling code must as well. Omitting the kwarg or setting it to ``None`` will
behave correctly without having to know that ``NotSet`` was used behind the
scenes to make it work.

The only time a caller would need to import ``NotSet`` is if they wanted to
proxy the do-not-care condition from the caller into the library. In that
case, you'd just do something like::

    from libperson import update
    from notset import NotSet

    def update_with_email(person, name=NotSet, age=NotSet):
        update(person, name=name, age=age)
        send_email(person)

With that in mind, go ahead, import ``notset`` and let your code stop caring.
