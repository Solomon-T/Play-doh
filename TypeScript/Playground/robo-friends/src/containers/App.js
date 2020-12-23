import React, { Component } from 'react';
import CardList from '../component/CardList'
// import { robots } from '../robots'
import SearchBox from '../component/SearchBox'
import Scroll from '../component/Scroll'
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
        const { robots, searchfield } = this.state;
        // Note this destructuring eliminates the need to use this.state
        const filteredRobots = robots.filter( robot => (
            robot.name.toLocaleLowerCase().includes(searchfield.toLocaleLowerCase())
        ))
        // console.log('render')

        if(!robots.length) return <h1 className='f1'> Loading </h1>
        
        return(
            <div className='tc'>
                <h1 className='f2'>Robo dudes</h1>
                <SearchBox searchChange={this.onSearchChange}/>
                <Scroll>
                    <CardList robots={filteredRobots}/>
                </Scroll>
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