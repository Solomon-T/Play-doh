import React, { useState, useEffect } from 'react';
import {connect} from 'react-redux';

import CardList from '../component/CardList'
import { classMates } from '../robots'
import SearchBox from '../component/SearchBox'
import Scroll from '../component/Scroll'
import './App.css'

import { setSearchField } from '../actions'

const mSP = state => {
    return {
        searchField: state.searchField
        // searchField: state.searchRobots.searchField
    }
}

const mDP = dispatch => {
    return {
        onSearchChange: (event) => dispatch(setSearchField(event.target.value))
    }
}

// always add an empty array to useEffect for it to act as component did mount
function App(props) {
    const robots = classMates
    // const [counts, setCounts] = useState(1)
    // const [robots, setRobots] = useState([])
    // const [searchfield, setSearchfield] = useState('')
    const { searchField, onSearchChange } = props

    useEffect(() => {
        console.log(props.store, 'component did mount')
        // console.log(counts, ' render')
    //     setCounts( counts + 1 )
    //     fetch('https://jsonplaceholder.typicode.com/users')
    //         .then(response => response.json())
    //         .then(users => setRobots(users))
    },[]);

    // const onSearchChange = (event) => {
    //     setSearchfield(event.target.value)
    // }

    const filteredRobots = robots.filter( robot => (
        robot.name.toLocaleLowerCase().includes(searchField.toLocaleLowerCase())
    ))

    if(!robots.length) return <h1 className='f1'> Loading </h1>
    
    return(
        <div className='tc'>
            <h1 className='f2'>Robo dudes</h1>
            <SearchBox searchChange={onSearchChange}/>
            <Scroll>
                <CardList robots={filteredRobots}/>
            </Scroll>
        </div>
    )
}



// class App extends Component{
//     constructor(){
//         super()
//         this.state = {
//             robots: [],
//             searchfield: ''
//         }
//         // console.log('constructor')
//     }

//     componentDidMount() {
//         // this.setState({robots: robots})
//         // console.log('componentDidMount')
//         // note fetch is part of the window object
//         fetch('https://jsonplaceholder.typicode.com/users')
//             .then(response => response.json())
//             .then(users => this.setState({robots: users}))

//     }

//     onSearchChange = (event) => {
//         this.setState({searchfield: event.target.value})
//     }

//     render(){   
//         const { robots, searchfield } = this.state;
//         // Note this destructuring eliminates the need to use this.state
//         const filteredRobots = robots.filter( robot => (
//             robot.name.toLocaleLowerCase().includes(searchfield.toLocaleLowerCase())
//         ))
//         // console.log('render')

//         if(!robots.length) return <h1 className='f1'> Loading </h1>
        
//         return(
//             <div className='tc'>
//                 <h1 className='f2'>Robo dudes</h1>
//                 <SearchBox searchChange={this.onSearchChange}/>
//                 <Scroll>
//                     <CardList robots={filteredRobots}/>
//                 </Scroll>
//             </div>
//         )
//     }
// }

export default connect(mSP,mDP)(App);