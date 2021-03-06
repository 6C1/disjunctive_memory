# Disjunctive Memory

## Overview

### Disjunctiveness

A [disjunctive sequence](https://en.wikipedia.org/wiki/Disjunctive\_sequence "Disjunctive Sequence on Wikipedia") over an alphabet _A_ is an infinite sequence, the finite subsequences of which include every finite combination of elements of _A_.

(From this point forward, all sequences described as disjunctive will be disjunctive over the alphabet _A_ = {0,1}.)

### The Idea

Given an arbitrary finite datum _d_ and an arbitrary disjunctive sequence _S_, there exists some nonnegative integer _n_ (the address of _d_) such that _S_[_n_,_n_+len(_d_)] = _d_.

Therefore, __a piece of data may be stored by just the triple (_S_,_n_,_d_).__

### Challenges

For an arbitrary data/sequence pair (_d_,_S_), the address _n_ will be larger to store than the original data (by the Pigeonhole Principle). However, for any data there exist infinitely many disjunctive sequences with arbitrarily small _n_. The size of _n_ can therefore be negotiated against savetime losses.

Furthermore, the task of producing an arbitrary digit of a given disjunctive sequence is nontrivial.

### Solutions

The growth of savetimes can be mitigated by parallelization and pluralization. Given a piece of data _d_ and a set of disjunctive sequences _S_, some number of sequences may be tested in parallel for _n_ values below a chosen threshold; as soon as the _n_ value associated with a particular sequence grows too large, that sequence may be discarded, and the thread applied to an as yet untested sequence.

Digit production can be handled by a subsystem.
