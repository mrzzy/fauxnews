import React from "react";

import "./imageHeading.css";

export default class ImageHeader extends React.Component {
    render() {
        return (
            <img styleName="img" src={this.props.src}/>
        );
    }
}