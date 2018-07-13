import React from "react";

import "./newsHeadline.css";

export default class NewsHeadline extends React.Component {
    render() {
        return (
            <h1 styleName="news-headline">{this.props.children}</h1>
        );
    }
}