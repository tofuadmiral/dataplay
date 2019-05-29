import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

class Square extends React.Component {

    // anything inside curly brackets is JSX code!!! 

    // each square should remember its state, private to that square
    // set this using the this.state thing 
    // make a constructor to initialize it

    constructor(props) {
        super(props); // inherit the supers props, always have to start w this 
        this.state={
            value: null, 
        };
    }

  render() { // draw from CSS to get square classname, and then show value 
            // use the arrow function notation 


    return (
      <button className="square" onClick={() => {this.setState({value: 'X'})}}>  
        {/* TODO */
            //this.props.value // shows the value of the square 
            // show the state 
            this.state.value
        }
      </button>
    );
  }
}

class Board extends React.Component {
  renderSquare(i) {
    return <Square value={i}/>; // changed to take in a value, which is i 
                // passing a prop from parent board to a child square, always flow from parent to children
  }

  render() {
    const status = 'Next player: X';

    return (
      <div>
        <div className="status">{status}</div>
        <div className="board-row">
          {this.renderSquare(0)}
          {this.renderSquare(1)}
          {this.renderSquare(2)}
        </div>
        <div className="board-row">
          {this.renderSquare(3)}
          {this.renderSquare(4)}
          {this.renderSquare(5)} 
        </div>
        <div className="board-row">
          {this.renderSquare(6)}
          {this.renderSquare(7)}
          {this.renderSquare(8)}
        </div>
      </div>
    );
  }
}

class Game extends React.Component {
  render() {
    return (
      <div className="game">
        <div className="game-board">
          <Board />
        </div>
        <div className="game-info">
          <div>{/* status */}</div>
          <ol>{/* TODO */}</ol>
        </div>
      </div>
    );
  }
}

// ========================================

ReactDOM.render(
  <Game />,
  document.getElementById('root')
);
