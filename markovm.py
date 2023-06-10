"""MarkovM: a Python library for Markov Models."""

from dataclasses import dataclass
from typing import Any, Generator, Iterable, Optional, Tuple

from numpy import float64, newaxis
from numpy.random import default_rng
from numpy.typing import NDArray

__version__: str = "0.0.1"


@dataclass(eq=False, frozen=True)
class MarkovModel:
    """Markov Model

    A stochastic model describing a sequence of possible events in which
    the probability of each event depends only on the state attained in
    the previous event.

    Attributes
    ----------
    state_space : tuple
        The collection of states in the Markov model.
    transition_matrix : NDArray
        The matrix describing the probabilities of transitions.
    """

    __slots__ = ["state_space", "transition_matrix"]

    state_space: tuple
    transition_matrix: NDArray[float64]


def create_markov_model(states: Iterable, transitions: NDArray) -> MarkovModel:
    """Create markov model.

    Provides an easy way to create a new Markov model and ensure the
    transition matrix is valid by normalizing the transition argument
    automatically.

    Parameters
    ----------
    states : Iterable
        The collection of states in the Markov model.
    transitions : NDArray
        The matrix to be normalized and serve as transition matrix.

    Returns
    -------
    MarkovModel
        A newly created markov model.

    Raises
    ------
    ValueError
        The shape of the transitions didn't match the total number of
        states. Given n states, the transitions matrix should be n by n.
    """
    # iterate though states and store as a tuple
    state_space = tuple(states)

    # verify if transition shape maches with state size
    num_of_states = len(state_space)
    if transitions.shape != (num_of_states, num_of_states):
        raise ValueError("shape misatch between states and transitions")

    # normalize tansitions
    transition_matrix = transitions / transitions.sum(axis=1)[:, newaxis]

    # create markov model and return
    return MarkovModel(state_space, transition_matrix)


def random_walk(
    model: MarkovModel, index: int = 0, seed: Optional[int] = None
) -> Generator[Any, None, None]:
    """Random walk through a markov model.

    Parameters
    ----------
    model : MarkovModel
        The Markov model contains states and transition probabilities.
    index : int, optional
        The index of the initial state, by default 0.
    seed : int, optional
        The seed to be used to generate random move, by default None.

    Yields
    ------
    state : Any
        The state after taking a step.

    Raises
    ------
    IndexError
        Invalid index of the initial state. Either less than zero or
        greater than the total number of states.
    """
    if not (0 <= index < len(model.state_space)):
        raise IndexError(f"index {index} is out of range")

    idxes = tuple(i for i, _ in enumerate(model.state_space))
    rng = default_rng(seed=seed)

    while True:
        yield model.state_space[index]
        index = rng.choice(idxes, p=model.transition_matrix[index])
