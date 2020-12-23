// import React, { Component } from 'react';

const Scroll = (props) => {
    // return <h1> Scrollable </h1>
    // return props.children
    return (
        <div style={{ overflowY: 'scroll', border: '5px solid black', height: '600px'}}>
            {props.children}
        </div>
    )
}

export default Scroll;
