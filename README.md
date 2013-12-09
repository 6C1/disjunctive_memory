# Disjunctive Memory

#### A system for small-size storage of big-size data

## Overview

Disjunctive Memory (D.M.) relies stores data using disjunctive numbers, id est irrational numbers whose digital expansions contain each possible finite sequence as subsequences. Given an arbitrary finite sequence of digits _d_ (data) and an arbitrary disjunctive number _x_, there exists a nonnegative integer _n_(_d,x_) such that the _n+m_-th digit of _x_ is identical to the _m_-th digit of _d_, for _m_ < len(_d_).

![Copeland–Erdős constant](http://upload.wikimedia.org/math/6/2/0/620dcd0f7275880369e51e7ce9b2da11.png)

For example, the Copeland–Erdős constant is the concatenation of "0." with the primes in ascending order (in base 10): x = 0.235711131719232931[...], and has been proven to be disjunctive. Given the data d = 7111, we may produce _n_(7111,_x_) = 3.

Disjunctive memory stores data in the form of the encrypted triple [_n_(_d,x_), len(_d_), *x], where *x is a pointer to the disjunctive number _x_.

## Design

The Disjunctive Memory system is designed around the following values:

* Small size

  The triple stored should be much smaller than the original data. This is achieved partly by outsourcing the disjunctive digit lookup to arbitrary systemic nodes.
* Security

  Each triple is encrypted via a standardized private key encryption scheme.
* Lookup speed

  D.M. selects lookup speed over save speed.

Rather than storing (or generating, or calculating) disjunctive numbers locally, D.M. includes a distributed, highly redundant set of disjunctive number nodes, each of which is publicly accessible and will return arbitrary digits of given disjunctive numbers with low latency. 

