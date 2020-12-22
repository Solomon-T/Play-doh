import React from 'react';
import 'tachyons';

const Card = () => {
    return(
        <div className= 'bg-light-green dib br3 pa3 ma2 grow bw2 shadow-5'>
            <img alt='profile photo' src='https://robohash.org/mkandala?size=200x200' />
            <div>
                <h2> Christopha Mkandala</h2>
                <p>chris@mkanda.com</p>
            </div>
        </div>
    )
}

export default Card;