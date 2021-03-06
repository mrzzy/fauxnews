import React from "react";

import Subtitle from "../common/Subtitle";
import "./faintSubtitle.css"

export default class FaintSubtitle extends React.Component {
    render() {
        return (
            <div styleName="faint-subtitle">
                <Subtitle {...this.props}></Subtitle>
            </div>
        );
    }
}