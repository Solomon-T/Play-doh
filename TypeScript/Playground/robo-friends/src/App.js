import React, { Component } from 'react';
import CardList from './CardList'
import { robots } from './robots'
import SearchBox from './SearchBox'
import './App.css'

class App extends Component{
    constructor(){
        super()
        this.state = {
            robots: [],
            searchfield: ''
        }
        // console.log('constructor')
    }

    componentDidMount() {
        // this.setState({robots: robots})
        // console.log('componentDidMount')
        // note fetch is part of the window object
        fetch('https://jsonplaceholder.typicode.com/users')
            .then(response => response.json())
            .then(users => this.setState({robots: users}))

    }

    onSearchChange = (event) => {
        this.setState({searchfield: event.target.value})
    }

    render(){    
        const filteredRobots = this.state.robots.filter( robot => (
            robot.name.toLocaleLowerCase().includes(this.state.searchfield.toLocaleLowerCase())
        ))
        // console.log('render')
        if(this.state.robots.length === 0){
            return <h1 className='f1'> Loading </h1>
        }
        return(
            <div className='tc'>
                <h1 className='f2'>Robo dudes</h1>
                <SearchBox searchChange={this.onSearchChange}/>
                <CardList robots={filteredRobots}/>
            </div>
        )
    }
}

// const App = () => {
//     return(
//         <div className='tc'>
//             <h2>Robo dudes</h2>
//             <SearchBox/>
//             <CardList robots={robots}/>
//         </div>
//     )
// }

export default App;