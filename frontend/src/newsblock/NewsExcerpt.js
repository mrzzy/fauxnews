import React from "react";

export default class NewsExcerpt extends React.Component {
    render() {
        return (
            <p>{this.props.children}</p>
        );
    }
}