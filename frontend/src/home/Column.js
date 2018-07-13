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
            // Add border styles between the rows
            var style = "item-row";
            if ((i+1) != children.length) {
                style += " border-bottom";
            }

            rows.push(
                <div key={i} className="row" styleName={style}>
                    {children[i]}
                </div>
            );
        }

        return (
            <div>{rows}</div>
        );
    }
}