import React from "react";

import "./subtitle.css";

export default class Subtitle extends React.Component {
    render() {
        var styles = "subtitle";
        if (this.props.alignLeft) {
            styles += " align-left";
        } else if (this.props.alignRight) {
            styles += " align-right";
        } else if (this.props.alignCenter) {
            styles += " align-center";
        }

        return (
            <h2 styleName={styles}>{this.props.children}</h2>
        );
    }
}