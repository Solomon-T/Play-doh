import React, { useState, useEffect } from 'react';
import {connect} from 'react-redux';

import CardList from '../component/CardList'
import SearchBox from '../component/SearchBox'
import Scroll from '../component/Scroll'
import './App.css'

import { setSearchField, requestRobots } from '../actions'

const mSP = state => {
    return {
        searchField: state.searchRobots.searchField,
        isPending: state.requestRobots.isPending,
        robots: state.requestRobots.robots,
        error: state.requestRobots.error
    }
}

const mDP = dispatch => {
    return {
        onSearchChange: (event) => dispatch(setSearchField(event.target.value)),
        onRequestRobots: () => dispatch(requestRobots())
    }
}

function App(props) {
    const { searchField, onSearchChange, robots } = props

    useEffect(() => {
        props.onRequestRobots();
    },[]);

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

export default connect(mSP,mDP)(App);