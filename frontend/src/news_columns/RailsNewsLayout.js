import React from "react";
import Column from "../home/Column";
import RailsLayout from "../common/RailsLayout";

export default class RailsNewsLayout extends React.Component {

    split_to_three(items) {
        var first = [];
        var second = [];
        var third = [];
        var all = [first, second, third];

        for (var i=0; i<items.length; i++) {
            all[i%3].push(items[i]);
        }

        return all;
    }
    
    render() {
        // If there are no children, return an empty div
        if (this.props.children == undefined) {
            return <div></div>;
        }

        // Move all the children to the children array
        var children = [];
        if (this.props.children.length == undefined) {
            // There is only one child
            children.push(this.props.children);
        } else {
            children = this.props.children;
        }

        // Split the children to three columns
        var cols = this.split_to_three(children);

        return (
            <RailsLayout>
                <Column>{cols[0]}</Column>
                <Column>{cols[1]}</Column>
                <Column>{cols[2]}</Column>
            </RailsLayout>
        );
    }
}