import React, {Component} from 'react'
// we destructure to avoid doing React.Component every single time
import './hello.css'
// just importing the css file in the component applies the styles. Sweet

// class Hello extends Component{
//     // each component must have a render funtion
//     render(){
//         // in case of returning multiple lines use brackets

//         // return <h1> My own Component?</h1>

//         return (
//             // this is tachyon
//             // Also take a look at how you pass in props
//             // How you use the passed props
//             <div className='f1 tc'>
//                 <h1> Hello from.. wait for it....</h1>
//                 <p> Welcome to the {this.props.userName} club</p>
//             </div>
//         )
//     }
// }

// for a funtional component to receive props 
function Hello(props){
    return(
        <div className='f1 tc'>
                <h1> Hello from.. wait for it....</h1>
                <p> Functional component from {props.userName} club</p>
            </div>
    )
}

export default Hello;


