import React from "react";
import invariant from "invariant";

export default class TripleLayout extends React.Component {
    componentWillMount() {
        invariant(this.props.children.length == 3,
                  "TripleLayout should have 3 child elements.");
    }

    render() {
        return (
            <div className="row">
                <div className="col-md">
                    {this.props.children[0]}
                </div>
                <div className="col-md">
                    {this.props.children[1]}
                </div>
                <div className="col-md">
                    {this.props.children[2]}
                </div>
            </div>
        );
    }
}