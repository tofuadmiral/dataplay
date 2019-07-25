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
      <button className="square" onClick={ () => this.props.onClick() }>  
        {/* TODO */
            //this.props.value // shows the value of the square 
            // show the state 
            this.props.value
        }
      </button>
    );
  }
}

class Board extends React.Component {

    // add a constructor so we can hold states here
    constructor(props){
        super(props);
        this.state = {
            squares: Array(9).fill(null), // pass this prop down to fill the specific square 
        }
    }


    // now adding some code to actually handle the click

    handleClick(i) {
        const squares = this.state.squares.slice();
        squares[i]='X';
        this.setState({squares: squares});
    }


  renderSquare(i) {
    return <Square value={this.state.squares[i]}
            // also hand down a function, onClick that the square can call
            // handle is a convention!!
            onClick={ () => this.handleClick(i)} // passing down this as a prop, the prop is a function!!!
         />;  // now, take the state value from parent board
    
    // changed to take in a value, which is i  
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