import React from "react";

import NewsThumbnail from "./NewsThumbnail";
import NewsTimestamp from "./NewsTimestamp";
import NewsHeadline from "./NewsHeadline";
import "./newsBlockLayout.css";

export default class NewsBlockLayout extends React.Component {
    render() {
        var thumbnail = null;
        if (this.props.thumbnailUrl) {
            thumbnail = <NewsThumbnail src={this.props.thumbnailUrl} />;
        }
        return (
            <div styleName="news-block">
                {thumbnail}
                <NewsTimestamp>{this.props.timestamp}</NewsTimestamp>
                <NewsHeadline>{this.props.headline}</NewsHeadline>
            </div>
        );
    }
}