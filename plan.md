# EMRK Manager - Complete Frontend Implementation Plan

## Phase 1: Core Layout & Global Navigation ✅
- [x] Set up base application layout with left sidebar navigation and top bar
- [x] Implement theme toggle system (dark/light mode) with state management
- [x] Create environment selector (Dev/Stage/Prod/Air-gapped) in top bar
- [x] Build engine filter dropdown and user profile menu
- [x] Design navigation sidebar with 8 main sections (Dashboard, Engines, Clusters, Nodes, Jobs, Telemetry, Logs, Settings)

---

## Phase 2: Dashboard & Engines Pages ✅
- [x] Build Global Dashboard page with summary cards (total engines, clusters, nodes, alerts)
- [x] Create Engine Status Overview section with health indicators
- [x] Add Environment Heatmap matrix (environments vs engines with color-coded status)
- [x] Implement Recent Events timeline with severity indicators
- [x] Create Engines List page with sortable table and status badges
- [x] Build Engine Detail View with tabs (Overview, Clusters, Telemetry, Logs, Plugin Info)

---

## Phase 3: Redis Cluster Detail & Topology ✅
- [x] Build Cluster Detail View header with cluster metadata and upgrade status
- [x] Create visual topology diagrams for Redis modes (Single, Replica, Sentinel, Cluster)
- [x] Implement Nodes tab with detailed node table (role, version, health, latency)
- [x] Build Plan & Apply tab with operation history and streaming logs
- [x] Add health-gate status panel and service startup failure handlers
- [x] Create Telemetry tab with time-series charts (latency, memory, failovers)
- [x] Build Config tab with YAML/JSON editor and validation

---

## Phase 4: Jobs, Telemetry & Logs Pages ✅
- [x] Create Jobs/Operations page with global operations table and job status tracking
- [x] Build Job Detail modal with steps, logs, and error troubleshooting
- [x] Implement Global Telemetry page with multi-engine charts and filters
- [x] Create Logs & Events page with advanced filtering (engine, cluster, severity, type)
- [x] Build Settings/Admin page with API config, environment definitions, plugin management

---

## Phase 5: UI Verification & Testing
- [ ] Test Jobs page - verify table, filters, job detail modal, and status badges
- [ ] Test Telemetry page - verify charts render, filters work, time range selector
- [ ] Test Logs page - verify search, severity filtering, and log display
- [ ] Test Settings page - verify all sections, plugin toggles, environment table
- [ ] Verify navigation between all pages works correctly
- [ ] Test dark/light theme toggle across all new pages
- [ ] Verify responsive design and mobile behavior