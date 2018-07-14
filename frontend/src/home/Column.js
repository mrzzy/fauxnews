import React from "react";

import "./column.css";

export default class Column extends React.Component {
    render() {
        // If there are no elements, return an empty div
        if (this.props.children === undefined) {
            return <div></div>;
        }

        // Store all the elements into an array
        var children = [];
        // If there is only one element, that element is returned instead of an
        // array.
        if (this.props.children.length === undefined) {
            children.push(this.props.children);
        } else {
            children = this.props.children;
        }

        var rows = [];
        for (var i=0; i<children.length; i++) {
            rows.push(
                <div key={i} className="row" styleName="item-row">
                    {children[i]}
                </div>
            );
        }

        return (
            <div styleName="container">{rows}</div>
        );
    }
}