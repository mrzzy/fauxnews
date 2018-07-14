import React from "react";

import "./newsHeadline.css";

export default class NewsHeadline extends React.Component {
    render() {
        var styles = "news-headline";
        if (this.props.hovering) {
            styles += " hovering";
        }
        return (
            <h1 styleName={styles}>{this.props.children}</h1>
        );
    }
}