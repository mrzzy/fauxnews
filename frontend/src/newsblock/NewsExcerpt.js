import React from "react";

import "./newsExcerpt.css";

export default class NewsExcerpt extends React.Component {
    render() {
        var styles = "excerpt";
        if (this.props.hovering) {
            styles += " hovering";
        }
        return (
            <p styleName={styles}>{this.props.children}</p>
        );
    }
}