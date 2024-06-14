import axios from 'axios';
import React, { useState, useEffect } from 'react';
import { Navigation } from "../../components/Navigation";
import { useParams, Link } from 'react-router-dom';
import {BACKEND_ADDRESS, FRONTEND_ADDRESS} from '../../constances';


export const View = () => {
    const { id } = useParams();

    return (
        <div>SIEMA WIDOK DZIECKA</div>
    );
}