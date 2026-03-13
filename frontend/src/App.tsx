import React from 'react';
import { DashboardLayout } from './layouts/DashboardLayout';
import { MetricsCards } from './components/MetricsCards';
import { TrainingProgressChart } from './components/TrainingProgressChart';

const App: React.FC = () => {
    return (
        <DashboardLayout>
            <h1>Dashboard</h1>
            <MetricsCards />
            <TrainingProgressChart />
        </DashboardLayout>
    );
};

export default App;