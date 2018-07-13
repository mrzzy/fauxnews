import React from "react";

import "./newsThumbnail.css";

export default class NewsThumbnail extends React.Component {
    render() {
        return (
            <img src={this.props.src} styleName="news-thumbnail" />
        );
    }
}