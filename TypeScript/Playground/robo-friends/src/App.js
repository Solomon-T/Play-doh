import React from 'react';
import CardList from './CardList'
import { robots } from './robots'

const App = () => {
    return(
        <div>
            <h2>Robo dudes</h2>
            <CardList robots={robots}/>
        </div>
    )
}

export default App;