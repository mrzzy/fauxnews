import React from "react";

import Subtitle from "../common/Subtitle";
import "./newsTimestamp.css";

export default class NewsSubtitle extends React.Component {
    render() {
        return (
            <div styleName="news-timestamp">
                <Subtitle alignLeft>{this.props.children}</Subtitle>
            </div>
        );
    }
}